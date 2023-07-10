import sys
import base64

def encode_user_id(user_id):
    encoded_id = base64.b64encode(user_id.encode()).decode()
    return encoded_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <userid>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    encoded_id = encode_user_id(user_id)
    print("Encoded User ID:", encoded_id)
