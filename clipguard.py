import psutil
import pyperclip
import PySimpleGUI as sg
from datetime import datetime
import re
import threading
import os


class ClipGuard:
    def __init__(self):
        self.suspicious_count = 0
        self.log_file = os.path.join(os.getcwd(), "clipguard_log.txt")
        print(f"Log file will be saved to: {self.log_file}")  # Debug
        self.running = True
        self.create_gui()

    def detect_crypto_addresses(self, text):
        """More reliable crypto detection"""
        crypto_keywords = ['bitcoin', 'btc', 'ethereum', 'eth', '0x', 'bc1']
        return (any(kw in text.lower() for kw in crypto_keywords)
                and len(text) > 20
                and not text.isspace())

    def monitor_clipboard(self, window):
        """Monitoring with better feedback"""
        last_value = pyperclip.paste()
        while self.running:
            current_value = pyperclip.paste()
            if current_value != last_value:
                event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_msg = f"Clipboard changed to: {current_value[:50]}... ({len(current_value)} chars)"

                # Always log the change
                self.log_event(log_msg)
                window.write_event_value('-LOG-', log_msg)

                # Check for crypto
                if self.detect_crypto_addresses(current_value):
                    alert_msg = f"🚨 CRYPTO DETECTED: {current_value[:30]}..."
                    self.log_event(alert_msg)
                    window.write_event_value('-ALERT-', alert_msg)
                    self.suspicious_count += 1
                    window['-COUNT-'].update(f"Alerts: {self.suspicious_count}")
                    window['-LOG-'].print(alert_msg, text_color='red')

                last_value = current_value
            sg.time.sleep(0.5)  # Check twice per second

    def log_event(self, message):
        """Guaranteed logging"""
        try:
            with open(self.log_file, "a", encoding='utf-8') as f:
                f.write(f"{datetime.now()}: {message}\n")
        except Exception as e:
            print(f"Failed to log: {e}")

    def create_gui(self):
        """Improved GUI"""
        sg.theme('DarkBlue3')

        layout = [
            [sg.Text("ClipGuard - Live Clipboard Monitor", font=('Helvetica', 16))],
            [sg.Text("Alerts: 0", key='-COUNT-', text_color='red')],
            [sg.Multiline(size=(70, 20), key='-LOG-', autoscroll=True, font=('Consolas', 10))],
            [sg.Button("Start", button_color=('white', 'green')),
             sg.Button("Stop", button_color=('white', 'orange')),
             sg.Button("Exit", button_color=('white', 'red'))]
        ]

        window = sg.Window("ClipGuard Forensic Tool", layout, finalize=True)

        # Auto-start monitoring
        threading.Thread(target=self.monitor_clipboard, args=(window,), daemon=True).start()

        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                self.running = False
                break
            elif event == "Stop":
                window['-LOG-'].print("Monitoring PAUSED", text_color='orange')
                self.running = False
            elif event == "Start":
                window['-LOG-'].print("Monitoring RESUMED", text_color='green')
                self.running = True
                threading.Thread(target=self.monitor_clipboard, args=(window,), daemon=True).start()

        window.close()


if __name__ == "__main__":
    print("Starting ClipGuard...")
    ClipGuard()