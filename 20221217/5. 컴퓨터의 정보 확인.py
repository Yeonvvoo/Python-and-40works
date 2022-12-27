# 컴퓨터 정보 확인 라이브러리
import psutil

# # cpu 속도
# cpu = psutil.cpu_freq()
# cpu_current = round(cpu.current / 1000, 2)
# print(f'cpu 속도: {cpu_current}GHz')
#
# # 물리 코어 수
# cpu_core = psutil.cpu_count(logical=False)
# print(f'cpu 코어: {cpu_core}개')
#
# # 메모리 정보
# memory = psutil.virtual_memory()
# # 메모리의 총량
# memory_total = round(memory.total / 1024 ** 3)
# print(f'메모리: {memory_total}GB')
#
# # 디스크 정보
# disk = psutil.disk_partitions()
# # 디스크 크기(있는 개수 만큼 다 출력)
# for i in disk:
#     # print(i.mountpoint, i.fstype, end='')
#     du = psutil.disk_usage(i.mountpoint)
#     disk_total = round(du.total / 1024 ** 3)
#     print(f'disk: {disk_total}GB')
#
# # 네트워크를 통해 보내고 받은 데이터량 출력
# net = psutil.net_io_counters()
# # 네트워크를 통해 보내고 받은 데이터 크기 출력(누적 데이터 값)
# sent = round(net.bytes_sent / 1024 ** 2, 1)
# recv = round(net.bytes_recv / 1024 ** 2, 1)
# print(f'보내기: {sent}MB, 받기: {recv}MB')

# 1초당 반복해서 정보 출력

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print(f'cpu 사용량: {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available / 1024**3, 1)
    print(f'사용 가능한 메모리: {memory_avail}GB')

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent, 1)
    recv = round(curr_recv-prev_recv, 1)
    print(f'보내기: {sent}MB, 받기: {recv}MB')

    prev_sent = curr_sent
    prev_recv = curr_recv