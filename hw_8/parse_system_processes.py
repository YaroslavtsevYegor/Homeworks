import subprocess
import datetime
import re


def parse_ps_aux_output():
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    output_lines = result.stdout.splitlines()

    users = set()
    process_count = {}
    memory_usage_total = 0
    cpu_usage_total = 0
    max_memory_process = ("", 0)
    max_cpu_process = ("", 0)

    for line in output_lines[1:]:
        parts = re.split(r'\s+', line)
        user = parts[0]
        cpu_percent = float(parts[2])
        rss_memory_mb = int(parts[5]) / 1024
        command = ' '.join(parts[10:])

        users.add(user)
        process_count[user] = process_count.get(user, 0) + 1
        memory_usage_total += rss_memory_mb
        cpu_usage_total += cpu_percent
        if rss_memory_mb > max_memory_process[1]:
            max_memory_process = (command[:20], rss_memory_mb)
        if cpu_percent > max_cpu_process[1]:
            max_cpu_process = (command[:20], cpu_percent)

    report = f"""
Отчет о состоянии системы ({datetime.datetime.now()}):
Пользователи системы: {', '.join(sorted(users))}
Процессов запущено: {len(output_lines)}
Пользовательские процессы:
{"\n".join(f"{u}: {c}" for u, c in sorted(process_count.items()))}
Всего памяти используется: {memory_usage_total:.1f} MB
Всего CPU используется: {cpu_usage_total:.1f}%
Больше всего памяти использует: {max_memory_process[0]} ({max_memory_process[1]:.1f} MB)
Больше всего CPU использует: {max_cpu_process[0]} ({max_cpu_process[1]:.1f}%)
"""

    filename = f'system_report_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.txt'
    with open(filename, 'w') as file:
        file.write(report)

    print(report)


if __name__ == "__main__":
    parse_ps_aux_output()
