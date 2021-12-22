import json
import yaml
from pathlib import Path

def update_image_uri(json_string_metadata, img_id, new_cid) -> json:
    img_uri = f'https://ipfs.io/ipfs/{new_cid}/cyberdoggo_{img_id:04d}_large.png'
    json_metadata = json.loads(json_string_metadata)
    json_metadata["image"] = img_uri
    return json_metadata


def main():
    # Load config with collection properties
    with open('config.yaml') as config:
        config = yaml.load(config, Loader=yaml.FullLoader)
    # Generate normal doggos (leave out legendary positions)
    for i in range(0, config['number']):
        meta_path = Path(config['build']) / str(i)
        updated_metadata = json.loads('{}')
        with open(meta_path) as metadata:
            updated_metadata = update_image_uri(metadata.read(), i, 'QmTPzX17YbW7KsM7Km5BNL4MX1mvCKHQrWynNJZfjgk57A')
        with open(meta_path, 'w') as f:
            f.write(json.dumps(updated_metadata))

if __name__ == "__main__":
    main()