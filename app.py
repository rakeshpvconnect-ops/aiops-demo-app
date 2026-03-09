from flask import Flask, jsonify
import os, time, random
 
app = Flask(__name__)
APP_VERSION = os.getenv('APP_VERSION', '2.0.0')
CONFIG_PATH = os.getenv('CONFIG_PATH', '/etc/app/config.yaml')
 
@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': APP_VERSION})
 
@app.route('/process')
def process():
    time.sleep(random.uniform(0.1, 0.3))
    return jsonify({'result': 'processed', 'version': APP_VERSION})
 
@app.route('/ready')
def ready():
    if not os.path.exists(CONFIG_PATH):
        return jsonify({'ready': False, 'reason': f'Missing {CONFIG_PATH}'}), 503
    return jsonify({'ready': True})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
