#!/bin/bash
pkill -9 streamlit
rm -rf /var/log/streamlit.log
nohup streamlit run "01_📝_Overview.py" 1>/var/log/streamlit.log 2>&1 &

