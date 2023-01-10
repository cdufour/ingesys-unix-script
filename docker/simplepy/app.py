import time
import os

# durée d'endormissement
duration = 5

# si la variable d'env est trouvée on écrase la valeur de duration
if "SLEEP_DURATION" in os.environ:
    duration = int(os.environ["SLEEP_DURATION"])

while True:
    print("Simple app (python) in infinite loop...")
    time.sleep(duration)