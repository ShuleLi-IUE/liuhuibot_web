#!/bin/bash

# 使用 pgrep 命令查找包含特定名称的进程
# -f 选项用于匹配完整的命令行
# -a 选项用于显示进程名和对应的命令行
# -l 选项用于显示进程名和对应的 PID
processes=$(pgrep -af "python web_ui_server.py")

if [ -n "$processes" ]; then
    # 打印找到的进程信息
    echo "Found the following processes matching 'python web_ui_server.py':"
    echo "$processes"

    # 提取 PID，然后逐个杀死进程
    while read -r pid cmdline; do
        echo "Killing process $pid..."
        kill "$pid"
    done <<< "$processes"

    echo "All matching processes killed."
else
    echo "No processes found matching 'python web_ui_server.py'."
fi

echo "kill down"

echo "strat server"
nohup python web_ui_server.py >> web_ui.log &
echo "strat server down"
