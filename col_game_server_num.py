from threading import Thread
import time




def weight_cal():
    ser_created_times = []
    for i in range(len(max_cpu)):
        avr = round(max_cpu[i] / sum(max_cpu),2)
        ser_created_times.append(round(avr * 500))
        # print(ser_created_times)
    return ser_created_times

def socket1(server_name,num):
    port_num = 0
    for i in range(int(num)):
        port_num += 1
        if port_num == 1:
            print('%s      %s'%(server_name,process_port_list[0]))
        elif port_num == 2:
            print('%s      %s'%(server_name,process_port_list[1]))
        elif port_num == 3:
            print('%s      %s'%(server_name,process_port_list[2]))
        elif port_num == 4:
            print('%s      %s'%(server_name,process_port_list[3]))
        elif port_num == 5:
            port_num = 1
            # print(port_num)
            print('%s      %s'%(server_name,process_port_list[0]))
            # continue
        time.sleep(0.5)
        # print(port_num)



if __name__ == "__main__":
    process_port_list = [50301, 50302, 50303, 50304]
    max_cpu = [6.3, 6.19, 11.62, 4.0, 9.3]
    threads = []
    weight_cal()
    weight_cal_return_list = weight_cal()

    for i in range(1,len(weight_cal_return_list)+1):
        server_name = 'socket-server' + str(i)
        t = Thread(target=socket1,args=(server_name,weight_cal_return_list[i-1],))
        t.start()
        time.sleep(0.01)
        threads.append(t)
    for t in threads:
        t.join()

    print('次数列表：%s\n 创服总数：%s'%(weight_cal_return_list,sum(weight_cal_return_list)))
