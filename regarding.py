import hashlib
import json
from datetime import datetime
from pathlib import Path

def stable_hash(a: str) -> str:
    return hashlib.sha256(a.encode('utf-8')).hexdigest()


def get_username() -> str:
    curr_file = Path(__file__).resolve()
    username = curr_file.parents[3].name
    return str(username)


def regard(n: int) -> None:
    username = get_username()
    now = datetime.now()
    super_secret_code = stable_hash(username + str(n) + str(now.year))
    json_file = Path('super_important.json')
    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {"hashes": []}
    data["hashes"].append(super_secret_code)
    with open('super_important.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    print(get_username())
