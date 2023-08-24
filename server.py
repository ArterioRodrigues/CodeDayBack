from flask import Flask, request, jsonify, make_response, send_from_directory, session
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader 
import io, os
import openai
from dotenv import load_dotenv


print("Hello WOrld)
