    Level 0
Key: -
Logging into overthewire using username: bandit0 and port 2220
ssh bandit0@bandit.labs.overthewire.org -p 2220

    Level 0-1
Key: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
Checking and reading the file 'readme' using ls and cat
ls
cat readme

    Level 1-2
Key: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
Checking and reading the file '-' using ls and cat. ./ is used because cat cannot read files with hyphen
ls
cat ./-

    Level 2-3
Key: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
Checking and reading the file 'spaces in this filename' using ls and cat. quotes are used because cat cannot read files with spaces
ls
cat 'spaces in this filename'

    Level 3-4
Key: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
Checking and using cd to change the directory to inhere. Checking and reading the file 'readme' using ls and cat
ls
cd inhere/
ls -al
cat ...Hidden-From-You

    Level 4-5
Key: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
Using cd to change the directory to inhere. Reading the files to find the one with password
cd inhere/
cat ./-file00
cat ./-file01
cat ./-file02
cat ./-file03
cat ./-file04
cat ./-file05
cat ./-file06
cat ./-file07

    Level 5-6
Key: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
Using cd to change the directory to inhere. Finding file based on size. Reading it using cat
cd inhere/
find . -size 1033c
cat ./maybehere07/.file2

    Level 6-7
Key: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
Using cd to change the directory to inhere. Findig file based on user, group and size. Reading it using cat
cd inhere/
find / -user bandit7 -group bandit6 -size 33c
cat /bandit7.password

    Level 7-8
Key: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
Using ls, cat and grep to check and read data.txt, then pattern match to find the password file
ls
cat data.txt | grep millionth

    Level 8-9
Key: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
Using ls to check data.txt, then sort to find the unique one
ls
sort data.txt | uniq -u

    Level 9-10
Key: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
Using ls, strings and grep to check and read data.txt, then pattern match to find the password file and strings to print only the text characters
ls
strings data.txt | grep =

    Level 10-11
Key: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
Using ls, cat and base64 to check, read and decode data.txt
ls
cat data.txt | base64 --decode

    Level 11-12
Key: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
Using ls, cat to check and read data.txt, then using python code to decrypt rot 13
ls
cat data.txt

    Level 12-13
Key: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
Initially a tmp directory is made and file is copied to it
    xxd -r is used to reverse hexdump the file
    then the compression is checked using file command and the following are done repeatedly to decompress it
    gzip -d - for gzip decompression
    bzip2 -d for bzip2 decompression
    tar -xvf for posix tar archive
mkdir /tmp/rithun
cp data.txt /tmp/rithun
cd /tmp/rithun
ls
file data.txt
xxd -r data.txt data1
ls
file data1
mv data1 data2.gz
gzip -d data2.gz
ls
file data2
mv data2 data3.bz2
bzip2 -d data3.bz2
ls
file data3
mv data3 data4.gz
gzip -d data4.gz
ls
file data4
tar -xvf data4
file data5.bin
tar -xvf data5.bin
file data6.bin
mv data6.bin data7.bz2
bzip2 -d data7.bz2
ls
file data7
tar -xvf data7
file data8.bin
mv data8.bin data9.gz
gzip -d data9.gz
ls
file data9
cat data9

    Level 13-14
Key: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Used scp to remote connect and get ssh key to login to bandit14 and used cat to read password
scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .  
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14

    Level 14-15
Key: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Connected to port 30000 via localhost
nc localhost 30000

    Level 15-16
Key: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Connected to port 30001 using ssl encryption
openssl s_client -connect localhost:30001

    Level 16-17
Key: EReVavePLFHtFlFsjn3hyzMlvSuSAcRD
Used nmap to find the available ports between 31000-32000 (5 ports, but only 2 ssl and one of them used echo) then used ncat to connect to the port
Then copied the RSA key to a tmp file using a text editor and got to level 17 using ssh
nmap -sV localhost -p 31000-32000
ncat --ssl localhost 31790
mkdir /tmp/random_sshkey
cd /tmp/random_sshkey
touch private.key
vim private.key
chmod 400 private.key
ssh -i private.key bandit17@localhost -p 2220
cat /etc/bandit_pass/bandit17

    Level 17-18
Key: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
Used sort and uniq to find the different password
sort passwords.old passwords.new | uniq -u


    Level 18-19
Key: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
Directly logged into the sh shell and used readme to get the key
ssh bandit18@bandit.labs.overthewire.org -p 2220 -t "/bin/sh"
cat readme

    Level 19-20
Key: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Read the bandit20-do file as bandit20 user
./bandit20-do cat /etc/bandit_pass/bandit20