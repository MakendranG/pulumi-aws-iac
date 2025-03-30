# Pulumi AWS Infrastructure as Code (IaC) Setup

This repository provides a streamlined approach to setting up AWS infrastructure using Pulumi with best practices for managing configurations and resources.

---

## **Prerequisites**
Before proceeding, ensure you have the following installed:

- Pulumi CLI ([Installation Guide](https://www.pulumi.com/docs/install/))
- AWS CLI configured with appropriate credentials ([Setup Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html))
- Python 3 and `pip` ([Download](https://www.python.org/downloads/))
- Git ([Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

---

## **Setup Process**

Follow these steps to set up your Pulumi AWS project:

### **1️⃣ Create a new project directory**
```sh
mkdir esc-challenge && cd esc-challenge
```

### **2️⃣ Initialize a new Pulumi AWS project**
```sh
pulumi new aws-python -y
```

### **3️⃣ Clone the repository**
```sh
git clone https://github.com/MakendranG/pulumi-aws-iac.git
```

### **4️⃣ Move infra folder and clean up**
```sh
mv pulumi-aws-iac/infra .
rm -rf pulumi-aws-iac
```

### **5️⃣ Ensure the correct entry point**
```sh
echo 'import infra.main' > __main__.py
```

### **6️⃣ Configure Pulumi secrets**
```sh
pulumi config set dbPassword 'my-secret-password' --secret
```

### **7️⃣ Refresh the stack to sync state**
```sh
pulumi refresh
```

### **8️⃣ Preview the deployment**
```sh
pulumi preview
```

### **9️⃣ Deploy the infrastructure**
```sh
pulumi up
```

---

## **Managing Your Stack**

### **Check Outputs**
After deployment, retrieve outputs using:
```sh
pulumi stack output
```

### **Destroying Resources**
To remove all resources:
```sh
pulumi destroy
```

To completely remove the stack:
```sh
pulumi stack rm
```

To delete the project folder completely:
```sh
cd .. && rm -rf esc-challenge
```

---

## **Project Structure**
```sh
esc-challenge/
│── infra/
│   ├── config.py
│   ├── main.py
│   ├── rds.py
│   ├── s3.py
│   ├── security_group.py
│── __main__.py  # Entry point
│── pulumi.dev.yaml
│── pulumi.yaml
│── requirements.txt
```

This structure ensures modularity and maintainability for AWS infrastructure using Pulumi.

---

## **Troubleshooting**

- If `pulumi up` fails due to authentication issues, verify your AWS credentials:
  ```sh
  aws sts get-caller-identity
  ```
- If errors occur due to missing dependencies, install them:
  ```sh
  pip install -r requirements.txt
  ```
- If `pulumi_aws` is not found, follow these steps:
  1. Activate the virtual environment:
     ```sh
     source venv/bin/activate  # For Linux/macOS
     ```
     ```sh
     venv\Scripts\activate  # For Windows
     ```
  2. Reinstall `pulumi_aws`:
     ```sh
     pip install --force-reinstall pulumi pulumi-aws
     ```
  3. Verify installation:
     ```sh
     pip list | grep pulumi-aws
     ```
  4. If not installed, try:
     ```sh
     pip install pulumi-aws --user
     ```
  5. Retry running Pulumi:
     ```sh
     pulumi up
     ```
- For debugging, use:
  ```sh
  pulumi logs -f
  ```

For more details, refer to [Pulumi Documentation](https://www.pulumi.com/docs/).

