# SSH - guide:

In this context `SSH` enables you establish remote communication between systems[client and remote host/server]. You can spawn a remote shell in this using `SSH` protocol.

## Prerequisites  

- all your Bash script files must be executable - i.e. do: `$ chmod +x filename`
- the first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`  
- environment:  
> - Ubuntu 20.04 LTS  
> - Bash shell  
> - Puppet   

## Steps:  
1. *ask for a server in the intranet* -> select [action] from the [Actions] drop-down menu.

<div>
    <img src="./ssh-png.png" height="100"/>
</div>

2. **`task 0` - Use a private key**:  
This is a demo on how to connect to your server; no restrictions. Follow the instructions in the task.
Ie you can connect to a remote host like this:  
```bash
# -i option is for specifying the identity file:
ssh -i path/to/file username@server-ip-address
```

3. **`task 1` - Create an SSH key pair**:  
This is how you create an SSH key-pair in command-line:
```bash
ssh-keygen -t type -b bit-length -C "some-identity-eg-machine-or-email"
```

This would take you through a wizard to specify path to file(path and its name - uses default type if you press enter) and then give a passphrase/blank to use none.  
So adapt this to be done using a bash script and specify the passphrase and the filename by passing in options for each respectively.


4. **`task 2` - Client configuration file**:  
This, and subsequent tasks, is the focus of this guide. 
Task specs:  
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:  
    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password
    Example:

```bash
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to 98.98.98.98 port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/school type -1
debug1: identity file /home/sylvain/.ssh/school-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_8.1
debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server->client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client->server aes128-ctr hmac-sha1-etm@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
debug1: Host '98.98.98.98' is known and matches the ECDSA host key.
debug1: Found key in /home/sylvain/.ssh/known_hosts:1
debug1: ssh_ecdsa_verify: signature correct
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/sylvain/.ssh/school
debug1: key_parse_private2: missing begin marker
debug1: read PEM private key done: type RSA
debug1: Authentication succeeded (publickey).
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
ubuntu@magic-server:~$
```

In the example above, we can see that `ssh` tries to authenticate using school and does not try to authenticate using a password. You can replace 98.98.98.98 by the IP of your server for testing purposes.  

> Well, you have to remember you generated a SSH key-pair in the project: `Bash - Loops, conditions and parsing`. This was a key-pair you generated in `task 0` of that project and you saved it to your intranet profile. It was used to setup your current SSH - Project to enable remote connection to your server.

> If you didn't, then sorry. Maybe you can do now and update in that project section though I think the public key is used to setup the current ssh project. So I'm not sure updating will help, unless the setup is done automatically, as in if there is a detetction mechanism that detects file changes in GitHub and adds the key from your GitHub to configure the new project dynamically.

Review these requirements again:

```bash 
    Your SSH client configuration must be configured to use the private key ~/.ssh/school  
    Your SSH client configuration must be configured to refuse to authenticate using a password  
```

> **Note** - focus on the first one:  
> Your key-pair generated in the project `Bash - Loops, conditions and parsing`, should exist in your local machine/sandbox/vm etc.
> If the key-pair you generated in the previous projcet is named `school`, and the path is `~/.ssh/school`, then you're good to go.  
> If not you might have to rename it to `school` ie rename public key, rename private key.  
>> `mv current-name school`  
>> `mv current-name.pub school.pub`  

> move both public key and private key to ~/.ssh/ directory:  
>> `mv school.pub school ~/.ssh/`  


### Configure Local OpenSSH Client:  

You should have a file `~/.ssh/config`  :
```bash
$ ls -a ~/.ssh/
```

If not create it:
```bash
vim ~/.ssh/config
```

Add the content below to whatever is inside if exists:
```bash
Host your-server-ip
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
```

Review this line in the console session above: `sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98`  

`Connect to your server`:  
If you asked for a server in step 1. You have an IP
```bash
ssh -v ubuntu@your-server-ip
```

If you get a `permission denied` error, set the file permission of the `~/.ssh/school` file to read-only for yourself/user:

```bash
chmod 400 ~/.ssh/school
```

Connect now: 
```bash
ssh -v ubuntu@your-server-ip
```

See shell session below for reference:

```bash
root@HP:/alx-SE/alx-system_engineering-devops/0x0B-ssh# ssh -v ubuntu@54.196.27.23
OpenSSH_8.2p1 Ubuntu-4ubuntu0.7, OpenSSL 1.1.1f  31 Mar 2020
debug1: Reading configuration data /root/.ssh/config
debug1: /root/.ssh/config line 1: Applying options for 54.196.27.23
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 54.196.27.23 [54.196.27.23] port 22.
debug1: Connection established.
debug1: identity file /root/.ssh/school type 0
debug1: identity file /root/.ssh/school-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.7
debug1: Remote protocol version 2.0, remote software version OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
debug1: match: OpenSSH_8.2p1 Ubuntu-4ubuntu0.5 pat OpenSSH* compat 0x04000000
debug1: Authenticating to 54.196.27.23:22 as 'ubuntu'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:2uWy4t4mrsUDCTW1ohb6RbkiVwBoU0C/bM6fLcjsTy8
debug1: Host '54.196.27.23' is known and matches the ECDSA host key.
debug1: Found key in /root/.ssh/known_hosts:7
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: Will attempt key: /root/.ssh/school RSA SHA256:GkR6pBszVUVA+c9UC7FyAVZMv0FaNn8RyRb5w/9+HgA explicit
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,sk-ssh-ed25519@openssh.com,ssh-rsa,rsa-sha2-256,rsa-sha2-512,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Offering public key: /root/.ssh/school RSA SHA256:GkR6pBszVUVA+c9UC7FyAVZMv0FaNn8RyRb5w/9+HgA explicit
debug1: Server accepts key: /root/.ssh/school RSA SHA256:GkR6pBszVUVA+c9UC7FyAVZMv0FaNn8RyRb5w/9+HgA explicit
debug1: Authentication succeeded (publickey).
Authenticated to 54.196.27.23 ([54.196.27.23]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: pledge: network
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:2: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Remote: /home/ubuntu/.ssh/authorized_keys:2: key options: agent-forwarding port-forwarding pty user-rc x11-forwarding
debug1: Sending environment.
debug1: Sending env LANG = C.UTF-8
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1021-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jun 25 08:53:59 UTC 2023

  System load:  0.08              Processes:             98
  Usage of /:   7.9% of 19.20GB   Users logged in:       0
  Memory usage: 22%               IPv4 address for eth0: 10.247.92.111
  Swap usage:   0%

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@194126-web-01:~$ ls
ubuntu@194126-web-01:~$ ls -a ~/.ssh/
.  ..  authorized_keys
ubuntu@194126-web-01:~$ cat ~/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCKAYwA7g+vnJ5XBV8lamCQo5jTaSJaJS6sMFYcaGhNWucItZjcKMdGj7lkleEFV2x00b9643oac0SeOXljTa3V4In7JlHV0Toot7SI7dZjE9Dgiq/+xRJmBZXs1MCf8QK5XS8rS+2i9JlXD52OZuX6iAqPo7ELASSf6PGyZotj+EdXSvq8bYfUoPW9HYDgfaxCpSgtnQ7tdTuZWjdCE+sBLpC+2Rl7s1LfNQWTQ5uPtXyxwUhrEWrwIClGMp5Wfl0N7DuX+3ZP6igaCDMtjgRCnqtvB27h0gQPHlV2zycf0bjGlHL7USSg/hNMm0EKdkPjcDEQAAkLRSF4OK+uQfU3 alx_applicant_server
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDS4g/rZhE9YRbJjgbZq46DZ7W2ZHD5auZn+Kv5tYaDsuSgL+7H4wYt3+9GHdOMOzXSTniDNs6A6sdAdH7vlpsXbDyZAuq+4EszLXafETcexx0HKocaKx3t77rFTmlqOfX6UFfT7rQxgyfZOG/mLWyxbZktSxG0htIBxeAW5X/nsj9n7YL/0MBsdZb6vKCZEJd6VU9mchWhcrklPvPvNH6TfvV/IJNAz0fnjP15U0mKENLmnSOnzrNq3vTYZ/SynDAjYz4ox1khT1AtpCbsZaJBY800JNvBVEEtWU0ymfEcSkKbPvdn5EU207KCEx+jwDDNsnD5zE2d6KH9UBIBHBeGhaZiuorbfbc5Uy/09Hhc3mUmq+jWCU3FIJJ7j44gqiWmp4AzfiC47w+ozks4Ze59+3UIl+7ULHZN5QteC6kupJL+nv6eL1WlimivvIQMKd3zIMireA4MU5IHe7Cf3lBUca4oIEx0iLE5qy65Sr46hUp62N7ulm2K6V8DfiTXevE= root@HP
ubuntu@194126-web-01:~$ nano ~/.ssh/authorized_keys
```

See below for contrast if the console text-above is jumbled up and some detail is not easily visible: 

![sever-shell](./server-shell.png)

<br/>

5. **Step n: task 3**  

While Still connected to your remote shell.(Review the last part of the console session above)  
Add the string(provided) to the `authorized_keys` file.  

```bash
nano ~/.ssh/authorized_keys
```

The SSH public key given in your intranet task 3 looks like this:
```bash
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

This is the end of the guide.

For task 4; follow the instructions and based on task requirements and your **Puppet** knowledge.
