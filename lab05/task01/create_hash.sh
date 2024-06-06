echo "MD5:" > hash.txt
md5sum personal.txt >> hash.txt

echo "SHA1:" >> hash.txt
sha1sum personal.txt >> hash.txt

echo "SHA224:" >> hash.txt
sha224sum personal.txt >> hash.txt

echo "SHA256:" >> hash.txt
sha256sum personal.txt >> hash.txt

echo "SHA384:" >> hash.txt
sha384sum personal.txt >> hash.txt

echo "SHA512:" >> hash.txt
sha512sum personal.txt >> hash.txt

echo "B2SUM:" >> hash.txt
b2sum personal.txt >> hash.txt
