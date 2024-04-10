# URLipy: URL Safety Checker

URLipy is a command-line tool written in Python for assessing the safety of URLs and associated IP addresses. It utilizes APIs to determine the risk of phishing and potential threats from IP addresses.

## Features
- Check the safety of URLs with HTTPS protocol.
- Assess the risk of phishing based on AI model predictions.
- Verify DNS records and domain age risk.
- Detect IP address presence in the URL.
- Determine if the URL is a shortened link.
- Evaluate URL reputation and blacklist status.
- Assess risks related to brute force attacks, SSH attacks, and URL redirection.
- Examine the risk level of low web traffic.

## Installation
1. Clone the repository: `git clone https://github.com/your_username/URLipy.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Obtain API keys from RapidAPI for Phishing URL Risk API and NetDetective API.
4. Replace the API keys in the code with your own.

## Usage
1. Run the `main.py` file: `python main.py`
2. Enter the URL you want to check.
3. Review the safety assessment and follow additional prompts to check associated IP addresses.

## External APIs
- Phishing URL Risk API: Used to assess the risk of phishing for the provided URL.
- NetDetective API: Used to examine the potential threats associated with IP addresses.

## License
URLipy is licensed under the [MIT License](https://github.com/your_username/URLipy/blob/main/LICENSE).

5. **Optional IP Address Check:**
   - URLipy offers an optional check for the associated IP address.
   - Users can choose to input an IP address to obtain additional details using a separate API.

6. **IP Address Details:**
   - For the optional IP address check, URLipy provides comprehensive information, covering various aspects of the IP address:
     - **VPN Status:** Indicates whether the IP address is associated with a VPN.
     - **Brute Force Attack Mode:** Alerts if the IP address is engaged in a brute force attack.
     - **Proxy Tunnel:** Identifies if the IP address is operating through a proxy tunnel.
     - **Infection Status:** Reports if the IP address is flagged for malware infections.
     - **DDoS Attack Mode:** Indicates if the IP address is involved in a Distributed Denial of Service (DDoS) attack.

7. **Exiting the Program:**
   - After providing comprehensive details, URLipy gracefully exits, completing the assessment process.

## Dependencies

URLipy relies on the following Python libraries:

- [pyfiglet](https://pypi.org/project/pyfiglet/): Used for ASCII art text formatting.
- [termcolor](https://pypi.org/project/termcolor/): Provides ANSI color formatting for the terminal.

Ensure these dependencies are installed before running the script.

## API Keys

Ensure possession of valid API keys for both the IPQualityScore and RapidAPI services. Update the key and X-RapidAPI-Key variables in the script with your respective API keys to facilitate seamless functionality.

## Disclaimer

URLipy leverages external APIs for URL and IP address information. Users are advised to ensure they possess the necessary permissions and comply with the terms of service of the utilized APIs.

## Customization

This README file serves as a foundation. Feel free to customize it further, adding specific details, examples, and screenshots to enhance its usability and cater to your intended audience.

## Author Information

- **Author:** Tornike Sonishvili
- **Contact:** sonishvili.tornike@gmail.com
- **City:** Georgia/Tbilisi
- **Youtube:** https://youtu.be/mZNwbySqSko

Tailor this README file to suit your preferences and the specific requirements of your users. Enhance user comprehension by providing usage examples, troubleshooting tips, and any additional information that may facilitate a smoother user experience. Keep the documentation updated for the benefit of your users. Consider integrating user testimonials, feature requests, or a brief project history to make the README more engaging and informative.