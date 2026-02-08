🔎 BTC Wallet Balance Checker (No API Key Required)
📌 Description

BTC Wallet Balance Checker is a lightweight Python tool designed to verify Bitcoin wallet balances in bulk without requiring any API key.
It allows users to scan large lists of Bitcoin addresses and retrieve their balances and transaction counts efficiently.

The tool queries public blockchain data sources and processes addresses in batches to improve performance while reducing request overload.

⚙️ Features

✅ Bulk Bitcoin address balance checking

✅ No API key required

✅ Batch processing for faster performance

✅ Progress bar display

✅ Transaction count retrieval

✅ Simple input/output text file support

✅ Automatic retry on connection errors

📥 Requirements
Python Version

Python 3.7+

Required Libraries

Install dependencies using:

pip install urllib3 tqdm

📄 Input File Format

The input file must contain one Bitcoin address per line.

Example:

1BoatSLRHtKNngkdXEeobR76b53LETtpyT
1Ez69SnzzmePmZX3WpEzMKTrcBF2gpNQ55
bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kygt080

▶️ Usage

Run the script using:

python balance.py input.txt output.txt

Arguments
Argument	Description
input.txt	File containing Bitcoin addresses
output.txt	Output file containing balance results
📊 Output Format

The output file will contain:

ADDRESS    BALANCE    TRANSACTION_COUNT


Example:

1BoatSLRHtKNngkdXEeobR76b53LETtpyT    0.01500000    12

🚀 How It Works

Loads all Bitcoin addresses from the input file

Sends requests in batches (default: 200 addresses per request)

Retrieves:

Final wallet balance

Number of transactions

Saves results into the output file

Displays a real-time progress bar

🔧 Configuration

You can modify these values inside the script:

LIMIT = 200   # Number of addresses per request
SATOSHI = 1e+8

⚠️ Disclaimer

This tool is intended for educational and research purposes only.
Users are responsible for complying with blockchain data provider usage policies.

❤️ Contribution

Feel free to fork the project and submit pull requests to improve functionality.

📜 License

MIT License (or specify your preferred license)
