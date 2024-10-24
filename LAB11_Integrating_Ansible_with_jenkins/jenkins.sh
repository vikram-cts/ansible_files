 sudo apt update -y
 sudo apt upgrade -y
 sudo apt install -y openjdk-17-jdk
 java --version
 curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
 echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
 sudo apt update -y
 sudo apt install -y jenkins
 sudo apt install sshpass
 sudo systemctl start jenkins
 sudo systemctl enable jenkins
 sudo systemctl status jenkins
 sudo apt update && sudo apt install ansible -y #for Ansible Installation