import firebase_admin
from firebase_admin import credentials, firestore

# CONFIG
SERVICE_ACCOUNT_PATH = "/home/pathfinder/pathfinder/firebase/ServiceAccountKey.json"
DEVICE_ID = "pathfinder_001"


def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)
    return firestore.client()


def reset_sos():
    db = init_firebase()

    db.collection("devices").document(DEVICE_ID).update({
        "sosActive": False,
        "lastUpdated": firestore.SERVER_TIMESTAMP
    })

    print(f"[SUCCESS] SOS reset for {DEVICE_ID}")


if __name__ == "__main__":
    reset_sos()