# PROTECTION ONLINE (Version 1)

_Identifies dark patterns online and summarizes the privacy policy of a website._
<br><br><br>


### 🌟 MILESTONES 🌟

🏆 Out of 25 teams competing at the college level, Our project was chosen as one of the six teams to advance to the Grand Finale round at IIT (BHU) Varanasi.
<br><br><br>


### PROTOTYPE VIDEO
https://github.com/raghavtwenty/protection-online/assets/126254197/3aee9def-7da3-4044-be07-50c5d99a86a3

<br><br>

### HOW TO EXECUTE

#### Terminal
```
git clone https://github.com/raghavtwenty/protection-online.git
```
<br>

```
cd protection-online/version_1/
```
<br>

#### Inside the version_1 project directory
Setup .env file 

```
REPLICATE_API_TOKEN = "Your API Key"
VIRUS_TOTAL_API_KEY = "Your API Key"
```
<br>

```
pip install -r requirements.txt
```
<br>

```
streamlit run main.py
```
<br>

#### Web Browser

```
http://127.0.0.1:8501/
```
<br>

### PROBLEM

Design and prototype innovative app or software-based solutions that can detect the use,type, and scale of dark patterns on e-commerce platforms.
<br><br><br>


### OUR OBJECTIVE

1. Privacy policy summarization <br>
2. Website cookie acceptance/rejection <br>
3. Detection of malicious URLs
<br><br><br>


### INTRODUCTION

Law enforcement and policies are changing from time to time especially in the cyber world. Users find it difficult and have no time to read the entire user agreement and privacy laws before using any application. The companies and application developers take advantage of it and make it even more difficult for the end users to show them fully on the data they collect from the users which are not necessary. Legitimate and malicious websites are hard to find for common users. To overcome the challenges we have stepped into "Protection Online". 
<br><br><br>


### TECHNOLOGIES USED

1. Generative AI <br>
2. Replicate <br>
3. LLM - Mixtral-8x7b-instruct-v0.1 <br>
4. Virus Total Malicious URL Analyzer <br>
5. WHOIS Database 
<br><br><br>


### WORKING

1. First the user enters the privacy policy link of a website or domain. <br>
2. Then it gathers the details about the domain from WHOIS database and checks for SSL Certification. <br>
3. After that it web scraps the complete privacy policy text of the domain. <br>
4. Now it passes the privacy policy to the LLM for summarization. <br>
5. Finally using Virus total API, It analyzes the domain for safety check and scoring. 
<br><br><br>


### END USERS

- All Internet users
<br><br><br>


### OUTPUTS

- Home Screen <br><br>
![1](https://github.com/raghavtwenty/protection-online/assets/126254197/f79d712c-ef61-489d-b7f2-778316f5d0c9)


- Website Information <br><br>
![2](https://github.com/raghavtwenty/protection-online/assets/126254197/c104cbec-8837-4857-bc81-1681fd0e2296)


- Data Collection Report <br><br>
![3](https://github.com/raghavtwenty/protection-online/assets/126254197/59f147a8-6069-439f-ac28-aaf9a354e38a)


- Security Report <br><br>
![4](https://github.com/raghavtwenty/protection-online/assets/126254197/33e8bdc7-0c65-455e-913e-923a9bbfd6e4)

<br>

### FUTURE ADD-ONS
1. User Friendly Extensions <br>
2. Multilingual Support <br>
3. Use of Local LLMs <br>
4. Use of RAG with DPDP Act, 2023
<br><br><br>


### DESIGNED & DEVELOPED BY
- RAGHAVA
<br><br>


_END OF README_
