package com.waitingforcode;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;
import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class DemoEncryptDecrypt {

    private static final String USER_KEY = "userkey1userkey1";

    public static void main(String[] args) throws NoSuchPaddingException, BadPaddingException, NoSuchAlgorithmException,
            IllegalBlockSizeException, UnsupportedEncodingException, InvalidKeyException {
        String encryptedBirthDate = encrypt("20.01.1980");
        System.out.println("Got encrypted birth date " + encryptedBirthDate);

        String decryptedBirthDate = decrypt(encryptedBirthDate);
        System.out.println("Got decrypted birth date " + decryptedBirthDate);
        System.out.println("Got decrypted birth date from Python " + decrypt("YUA+4n6qUK4QaoNt6AbL3g=="));
    }

    private static String encrypt(String valueToEncrypt) throws NoSuchPaddingException,
            NoSuchAlgorithmException, UnsupportedEncodingException, InvalidKeyException, BadPaddingException,
            IllegalBlockSizeException {
        SecretKeySpec secretKeySpec = new SecretKeySpec(USER_KEY.getBytes("UTF-8"), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);

        byte[] cipherBytes = cipher.doFinal(valueToEncrypt.getBytes("UTF-8"));
        byte[] messageBytes = new byte[cipherBytes.length];

        System.arraycopy(cipherBytes, 0, messageBytes, 0, cipherBytes.length);
        return new String(Base64.getEncoder().encode(messageBytes), "UTF-8");
    }

    private static String decrypt(String base64ValueToDecrypt) throws UnsupportedEncodingException,
            NoSuchPaddingException, NoSuchAlgorithmException, InvalidKeyException, BadPaddingException,
            IllegalBlockSizeException {
        System.out.println("Decrypting "+base64ValueToDecrypt);
        SecretKeySpec secretKeySpec = new SecretKeySpec(USER_KEY.getBytes("UTF-8"), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);
        byte[] byte_array = cipher.doFinal(Base64.getDecoder().decode(base64ValueToDecrypt));
        return new String(byte_array, StandardCharsets.UTF_8);
    }

}
