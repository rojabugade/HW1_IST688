{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1dOuhVkI-xWaRd-Pjve1nflB8XlMY9rYw",
      "authorship_tag": "ABX9TyMpeyytCkB3nudwuZOMg5PP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rojabugade/HW1_IST688/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IHXXPXq9QLGQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b2c67742-ecfc-4a86-a473-e7acd80d836b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.38.0-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting PyMuPDF\n",
            "  Downloading PyMuPDF-1.24.10-cp310-none-manylinux2014_x86_64.whl.metadata (3.4 kB)\n",
            "Collecting openai\n",
            "  Downloading openai-1.46.0-py3-none-any.whl.metadata (24 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (10.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.8.1)\n",
            "Collecting tenacity<9,>=8.1.0 (from streamlit)\n",
            "  Downloading tenacity-8.5.0-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<5,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl.metadata (38 kB)\n",
            "Collecting PyMuPDFb==1.24.10 (from PyMuPDF)\n",
            "  Downloading PyMuPDFb-1.24.10-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (1.4 kB)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from openai) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from openai) (1.7.0)\n",
            "Collecting httpx<1,>=0.23.0 (from openai)\n",
            "  Downloading httpx-0.27.2-py3-none-any.whl.metadata (7.1 kB)\n",
            "Collecting jiter<1,>=0.4.0 (from openai)\n",
            "  Downloading jiter-0.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.6 kB)\n",
            "Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from openai) (2.9.1)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from openai) (1.3.1)\n",
            "Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.10/dist-packages (from openai) (4.66.5)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (3.10)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->openai) (1.2.2)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->openai) (2024.8.30)\n",
            "Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai)\n",
            "  Downloading httpcore-1.0.5-py3-none-any.whl.metadata (20 kB)\n",
            "Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->openai)\n",
            "  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->openai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.23.3 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->openai) (2.23.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.38.0-py2.py3-none-any.whl (8.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.7/8.7 MB\u001b[0m \u001b[31m55.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading PyMuPDF-1.24.10-cp310-none-manylinux2014_x86_64.whl (3.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.5/3.5 MB\u001b[0m \u001b[31m59.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading PyMuPDFb-1.24.10-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (15.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.9/15.9 MB\u001b[0m \u001b[31m42.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading openai-1.46.0-py3-none-any.whl (375 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m375.0/375.0 kB\u001b[0m \u001b[31m20.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m9.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpx-0.27.2-py3-none-any.whl (76 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m76.4/76.4 kB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpcore-1.0.5-py3-none-any.whl (77 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.9/77.9 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jiter-0.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (318 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m318.9/318.9 kB\u001b[0m \u001b[31m18.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m57.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tenacity-8.5.0-py3-none-any.whl (28 kB)\n",
            "Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.9/82.9 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m4.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m4.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: watchdog, tenacity, smmap, PyMuPDFb, jiter, h11, PyMuPDF, pydeck, httpcore, gitdb, httpx, gitpython, openai, streamlit\n",
            "  Attempting uninstall: tenacity\n",
            "    Found existing installation: tenacity 9.0.0\n",
            "    Uninstalling tenacity-9.0.0:\n",
            "      Successfully uninstalled tenacity-9.0.0\n",
            "Successfully installed PyMuPDF-1.24.10 PyMuPDFb-1.24.10 gitdb-4.0.11 gitpython-3.1.43 h11-0.14.0 httpcore-1.0.5 httpx-0.27.2 jiter-0.5.0 openai-1.46.0 pydeck-0.9.1 smmap-5.0.1 streamlit-1.38.0 tenacity-8.5.0 watchdog-4.0.2\n",
            "\u001b[K\u001b[?25h\n",
            "added 22 packages, and audited 23 packages in 2s\n",
            "\n",
            "3 packages are looking for funding\n",
            "  run `npm fund` for details\n",
            "\n",
            "1 \u001b[33m\u001b[1mmoderate\u001b[22m\u001b[39m severity vulnerability\n",
            "\n",
            "To address all issues (including breaking changes), run:\n",
            "  npm audit fix --force\n",
            "\n",
            "Run `npm audit` for details.\n"
          ]
        }
      ],
      "source": [
        "# Install required libraries\n",
        "!pip install streamlit PyMuPDF openai\n",
        "!npm install -g localtunnel"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Mount Google Drive\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fhvb-ODTQqUD",
        "outputId": "17ce6898-1bb1-4351-fb2d-c50a4e3362f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Change to the desired directory\n",
        "import os\n",
        "os.chdir(\"/content/drive/MyDrive/IST688\")"
      ],
      "metadata": {
        "id": "W-FPygSFQ-XL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q -r requirements.txt"
      ],
      "metadata": {
        "id": "vwH_1e_LXXpD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Print the public IP address\n",
        "import urllib\n",
        "print(\"Password/Endpoint IP for localtunnel is:\", urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZBYqaXiaRK9Q",
        "outputId": "abf93668-20e6-47e1-9ac6-33e08f9bd960"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Password/Endpoint IP for localtunnel is: 34.19.67.75\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Write the Streamlit app code to app.py\n",
        "with open('app.py', 'w') as f:\n",
        "    f.write('''\n",
        "import streamlit as st\n",
        "import fitz  # PyMuPDF for handling PDF files\n",
        "from openai import OpenAI\n",
        "\n",
        "# Function to validate and read PDF files using PyMuPDF\n",
        "def read_pdf(file):\n",
        "    doc = fitz.open(stream=file.read(), filetype=\"pdf\")\n",
        "    text = \"\"\n",
        "    for page in doc:\n",
        "        text += page.get_text()\n",
        "    return text\n",
        "\n",
        "# Show title and description\n",
        "st.title(\"📄 RBHomeWorkMate\")\n",
        "st.write(\n",
        "    \"Upload a document below and ask a question about it – GPT will answer! \"\n",
        ")\n",
        "\n",
        "# Ask user for their OpenAI API key via `st.text_input`\n",
        "openai_api_key = st.text_input(\"OpenAI API Key\", type=\"password\")\n",
        "if not openai_api_key:\n",
        "    st.info(\"Please add your OpenAI API key to continue.\", icon=\"🗝️\")\n",
        "else:\n",
        "    try:\n",
        "        # Create an OpenAI client with the provided API key\n",
        "        client = OpenAI(api_key=openai_api_key)\n",
        "    except Exception as e:\n",
        "        st.error(f\"Failed to initialize OpenAI client: {e}\")\n",
        "        st.stop()\n",
        "\n",
        "    # Let the user upload a file via `st.file_uploader`\n",
        "    uploaded_file = st.file_uploader(\n",
        "        \"Upload a document (.txt, .md, or .pdf)\", type=(\"txt\", \"md\", \"pdf\")\n",
        "    )\n",
        "\n",
        "    # Ask the user for a question via `st.text_area`\n",
        "    question = st.text_area(\n",
        "        \"Now ask a question about the document!\",\n",
        "        placeholder=\"Can you give me a short summary?\",\n",
        "        disabled=not uploaded_file,\n",
        "    )\n",
        "\n",
        "    # If a file is uploaded and a question is asked\n",
        "    if uploaded_file and question:\n",
        "        try:\n",
        "            # Read the uploaded file based on its extension\n",
        "            file_extension = uploaded_file.name.split('.')[-1]\n",
        "            if file_extension in ['txt', 'md']:\n",
        "                document = uploaded_file.read().decode()\n",
        "            elif file_extension == 'pdf':\n",
        "                document = read_pdf(uploaded_file)\n",
        "            else:\n",
        "                st.error(\"Unsupported file type.\")\n",
        "                st.stop()\n",
        "\n",
        "            # Prepare the message for GPT model\n",
        "            messages = [\n",
        "                {\n",
        "                    \"role\": \"user\",\n",
        "                    \"content\": f\"Here's a document: {document} {question}\",\n",
        "                }\n",
        "            ]\n",
        "\n",
        "            # Generate an answer using the OpenAI API\n",
        "            stream = client.chat.completions.create(\n",
        "                model=\"gpt-4o-mini\",  # Ensure the model name is correct\n",
        "                messages=messages,\n",
        "                stream=True,\n",
        "            )\n",
        "\n",
        "            # Initialize an empty string to accumulate the response\n",
        "            response_text = \"\"\n",
        "\n",
        "            # Iterate through each chunk in the stream\n",
        "            for chunk in stream:\n",
        "                # Check if the chunk has choices and delta attributes\n",
        "                if hasattr(chunk, 'choices') and hasattr(chunk.choices[0], 'delta'):\n",
        "                    # Extract the delta content safely, ensuring it's a string\n",
        "                    delta_content = getattr(chunk.choices[0].delta, 'content', '')\n",
        "                    if delta_content:  # Only concatenate if content is not None\n",
        "                        response_text += delta_content\n",
        "                else:\n",
        "                    st.error(\"Unexpected response structure.\")\n",
        "\n",
        "            # Display the accumulated response text all at once\n",
        "            st.write(response_text)\n",
        "\n",
        "        except Exception as e:\n",
        "            st.error(f\"An error occurred while processing your request: {e}\")\n",
        "    ''')\n"
      ],
      "metadata": {
        "id": "81d2NPooYxvx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "id": "vPsMZ1lvT7rr",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cc0235dc-5cb7-43e7-930f-9a3c75ec4d44"
      },
      "execution_count": null,
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "your url is: https://hip-shrimps-share.loca.lt\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.19.67.75:8501\u001b[0m\n",
            "\u001b[0m\n"
          ]
        }
      ]
    }
  ]
}