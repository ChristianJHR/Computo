
usuario@usuario-VirtualBox:~/haproxylb/containerized$ siege -c 100 -i -b -v -t 5m http://localhost:8083

{	"transactions":			      874784,
	"availability":			      100.00,
	"elapsed_time":			      299.53,
	"data_transferred":		      513.07,
	"response_time":		        0.03,
	"transaction_rate":		     2920.52,
	"throughput":			        1.71,
	"concurrency":			       98.73,
	"successful_transactions":	      874784,
	"failed_transactions":		           0,
	"longest_transaction":		        1.49,
	"shortest_transaction":		        0.00
}


ab -c 100 -t 300 http://localhost:8083/
This is ApacheBench, Version 2.3 <$Revision: 1903618 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:        nginx/1.27.5
Server Hostname:        localhost
Server Port:            8083

Document Path:          /
Document Length:        615 bytes

Concurrency Level:      100
Time taken for tests:   6.474 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42400000 bytes
HTML transferred:       30750000 bytes
Requests per second:    7723.61 [#/sec] (mean)
Time per request:       12.947 [ms] (mean)
Time per request:       0.129 [ms] (mean, across all concurrent requests)
Transfer rate:          6396.12 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   1.2      0      18
Processing:     2   12   5.4     11      72
Waiting:        0   12   5.0     11      47
Total:          2   13   5.5     12      73

Percentage of the requests served within a certain time (ms)
  50%     12
  66%     14
  75%     15
  80%     17
  90%     20
  95%     23
  98%     27
  99%     31
 100%     73 (longest request)
