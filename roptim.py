import threading
import random

target = 48
guess = random.uniform(0.0, float(target))
lr = 0.01
lock = threading.Lock()  # To safely update the shared guess variable

def optimize_guess():
    global guess
    while abs(guess - target) > 0.01:
        error = target - guess
        with lock:  # Only one thread updates the guess at a time
            if guess < target:
                guess = random.uniform(guess, target)
            else:
                guess = random.uniform(target, guess)
        print(f"Guess: {guess}, Target: {target}, Error: {error}")

# Create multiple threads
threads = []
for _ in range(4):  # Number of threads
    t = threading.Thread(target=optimize_guess)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"Final Guess: {guess}")
