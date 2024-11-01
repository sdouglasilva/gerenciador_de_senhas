import string, secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet

class FernetHasher:
  RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
  BASE_DIR = Path(__file__).resolve().parent.parent
  KEY_DIR = BASE_DIR / 'keys'

  def __init__(self,key) -> None:
    print('Olá Mundo')
    if not isinstance(key, bytes):
      key = key.encode()
    self.fernet = Fernet(key)

  @classmethod
  def _get_random_string(cls, length=25):
    string = ''
    for i in range(length):
      string+=(secrets.choice(cls.RANDOM_STRING_CHARS))
    return string
  
  @classmethod
  def create_key(cls, archive = False):
    value = cls._get_random_string()
    value = value.encode('utf-8')
    hasher = hashlib.sha256(value).digest()
    key = base64.b64encode(hasher)
    if archive:
      return key, cls.archive_key(key)
    return key, None

  @classmethod
  def archive_key(cls,key):
    file = 'key.txt'
    while Path(cls.KEY_DIR / file).exists():
      file = f'key_{cls._get_random_string(length=5)}.key'
    with open(cls.KEY_DIR / file, 'wb') as  arq :
      arq.write(key)
      return cls.KEY_DIR / file
    
  def encrypt(self,value):
        if not isinstance(value, bytes):
          value = value.encode()
        return self.fernet.encrypt(value)
  
  def decrypt(self,value):
      if not isinstance(value, bytes):
        value = value.encode()
      return self.fernet.encrypt(value)

# FernetHasher.create_key(archive=True)

fernet_douglas = FernetHasher('rHmj6fuJdQEghVaJT3R0vlNDjusVBf4zTZwEXe4qJ9c=')
print(fernet_douglas.decrypt('Minha senha'))