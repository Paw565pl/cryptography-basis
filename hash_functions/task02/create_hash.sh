echo "MD5:" > hash.txt
cat hash-.pdf personal.txt | md5sum >> hash.txt
cat hash-.pdf personal_.txt | md5sum >> hash.txt

echo "SHA1:" >> hash.txt
cat hash-.pdf personal.txt | sha1sum >> hash.txt
cat hash-.pdf personal_.txt | sha1sum >> hash.txt

echo "SHA224:" >> hash.txt
cat hash-.pdf personal.txt | sha224sum >> hash.txt
cat hash-.pdf personal_.txt | sha224sum >> hash.txt

echo "SHA256:" >> hash.txt
cat hash-.pdf personal.txt | sha256sum >> hash.txt
cat hash-.pdf personal_.txt | sha256sum >> hash.txt

echo "SHA384:" >> hash.txt
cat hash-.pdf personal.txt | sha384sum >> hash.txt
cat hash-.pdf personal_.txt | sha384sum >> hash.txt

echo "SHA512:" >> hash.txt
cat hash-.pdf personal.txt | sha512sum >> hash.txt
cat hash-.pdf personal_.txt | sha512sum >> hash.txt

echo "B2SUM:" >> hash.txt
cat hash-.pdf personal.txt | b2sum >> hash.txt
cat hash-.pdf personal_.txt | b2sum >> hash.txt
