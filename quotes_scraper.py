{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dca86102-366c-41d7-991d-4e885e28f282",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (2.32.3)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (4.12.3)\n",
      "Requirement already satisfied: pandas in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from requests) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from requests) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from requests) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from requests) (2024.8.30)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from beautifulsoup4) (2.5)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\hhhxf\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests beautifulsoup4 pandas\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e2842487-91e3-4849-ba9c-71556ec0c9b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Daten gespeichert in quotes.csv\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# URL der Zielseite\n",
    "URL = \"http://quotes.toscrape.com/\"\n",
    "\n",
    "# HTTP-Header\n",
    "HEADERS = {\n",
    "    \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36\"\n",
    "}\n",
    "\n",
    "def fetch_page(url):\n",
    "    \"\"\"Holt die HTML-Seite.\"\"\"\n",
    "    response = requests.get(url, headers=HEADERS)\n",
    "    if response.status_code == 200:\n",
    "        return response.text\n",
    "    else:\n",
    "        print(f\"Fehler: {response.status_code}\")\n",
    "        return None\n",
    "\n",
    "def parse_page(html):\n",
    "    \"\"\"Extrahiert Zitate, Autoren und Tags.\"\"\"\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "    quotes = []\n",
    "    for quote in soup.select(\".quote\"):\n",
    "        text = quote.select_one(\".text\").text.strip()\n",
    "        author = quote.select_one(\".author\").text.strip()\n",
    "        tags = [tag.text.strip() for tag in quote.select(\".tag\")]\n",
    "        quotes.append({\"Quote\": text, \"Author\": author, \"Tags\": \", \".join(tags)})\n",
    "    return quotes\n",
    "\n",
    "def save_to_csv(data, filename=\"quotes.csv\"):\n",
    "    \"\"\"Speichert Daten in einer CSV-Datei.\"\"\"\n",
    "    df = pd.DataFrame(data)\n",
    "    df.to_csv(filename, index=False)\n",
    "    print(f\"Daten gespeichert in {filename}\")\n",
    "\n",
    "# Ablauf\n",
    "if __name__ == \"__main__\":\n",
    "    # HTML-Seite abrufen\n",
    "    html_content = fetch_page(URL)\n",
    "    if html_content:\n",
    "        # Daten extrahieren\n",
    "        quotes_data = parse_page(html_content)\n",
    "        # Daten speichern\n",
    "        save_to_csv(quotes_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4a8bddca-2370-4c40-9be0-0de78967608d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                               Quote           Author  \\\n",
      "0  “The world as we have created it is a process ...  Albert Einstein   \n",
      "1  “It is our choices, Harry, that show what we t...     J.K. Rowling   \n",
      "2  “There are only two ways to live your life. On...  Albert Einstein   \n",
      "3  “The person, be it gentleman or lady, who has ...      Jane Austen   \n",
      "4  “Imperfection is beauty, madness is genius and...   Marilyn Monroe   \n",
      "\n",
      "                                           Tags  \n",
      "0        change, deep-thoughts, thinking, world  \n",
      "1                            abilities, choices  \n",
      "2  inspirational, life, live, miracle, miracles  \n",
      "3              aliteracy, books, classic, humor  \n",
      "4                    be-yourself, inspirational  \n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"quotes.csv\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "27bc9f0c-3ad8-4d85-baa3-074bd3ce9b5a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3999121736.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[18], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    python quotes_scraper.py\u001b[0m\n\u001b[1;37m           ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "python quotes_scraper.py"
   ]
  },
  {
   "cell_type": "code",
  "execution_count": None,
   "id": "1bbd7531-9be3-4b90-be00-40e2a95f07a3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
