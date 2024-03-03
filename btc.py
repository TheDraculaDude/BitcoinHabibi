import itertools
import subprocess
import requests
def calculate_wallet_balance(seed_phrase):
  def generate_permutations(fixed_words, remaining_length):
    return itertools.product(fixed_words, repeat=remaining_length)

def main():
  fixed_words=input("Enter 8 fixed: ").split()
  if len(fixed_words) !=8:
    print("Please enter 8 words.")
    return

remaining_words = input("Enter 16 words: ").split()
if len(remaining_words) !=16:
  print("please enter 16 words.")
  return

all_permutations = generate_permutations(remaining_words, 16)
for permutation in all_permutations:
  seed_phrase = " ".join(fixed_words + list(permutation))
  balance = calculate_wallet_balance(seed_phrase)

print(f"Seed Phrase: {seed_phrase}\nWallet Balance: {Balance} BTC\n")
balance_usd = balance * current_btc_to_usd_rate
print(f"Balance in USD: {balance_usd} USD\n")
if balance > 0.0000001:
  print("Bitcoin found. Stopping")
  break

if __name__ = "__main__":
current_btc_to_usd_rate = 50000
main()
