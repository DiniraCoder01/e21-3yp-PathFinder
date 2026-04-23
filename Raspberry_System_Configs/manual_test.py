from send_sos import send_sos_alert
from reset_sos import reset_sos

if __name__ == "__main__":
    while True:
        cmd = input("Enter command (sos/reset/exit): ").strip().lower()

        if cmd == "sos":
            send_sos_alert()
        elif cmd == "reset":
            reset_sos()
        elif cmd == "exit":
            print("Exiting...")
            break
        else:
            print("Unknown command")