import pyperclip
import time


def simulate_attack():
    print("=== STARTING ATTACK SIMULATION ===")
    print("Copying Bitcoin address to clipboard...")
    original_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"  # Real Bitcoin genesis address
    malicious_address = "1FakeAddressForStealingCoins"

    pyperclip.copy(original_address)
    print(f"Original: {original_address}")
    time.sleep(3)  # Give detector time to notice

    print("\nAttacker replacing clipboard...")
    pyperclip.copy(malicious_address)
    print(f"Malicious: {pyperclip.paste()}")
    print("\n=== ATTACK COMPLETE ===")


if __name__ == "__main__":
    simulate_attack()