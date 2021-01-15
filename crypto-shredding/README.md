# Demo steps

## PostgreSQL
1. `docker-compose down --volumes; docker-compose up`
2. `docker exec -ti crypto-shredding_postgresql_1 bash` 
3. `psql --u bartosz --password -d wfc_cryptoshredding`
4. Decrypted encrypted data elsewhere: `SELECT CONVERT_FROM(DECRYPT(DECODE('YUA+4n6qUK4QaoNt6AbL3g==', 'base64'), 'userkey1userkey1', 'aes'), 'UTF-8');`
5. Encrypt data: `SELECT ENCODE(ENCRYPT('20.01.1980', 'userkey1userkey1', 'aes'), 'base64');`

## Java
1. Launch the `DemoEncryptDecrypt` class.

## Python
1. Launch the `demo_encrypt_decrypt` file.
