usuario@usuario-VirtualBox:~/haproxylb/containerized$ ab -n 3000 -c 100 -t 300 http://localhost:8083/
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
Time taken for tests:   6.197 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42400000 bytes
HTML transferred:       30750000 bytes
Requests per second:    8068.52 [#/sec] (mean)
Time per request:       12.394 [ms] (mean)
Time per request:       0.124 [ms] (mean, across all concurrent requests)
Transfer rate:          6681.75 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   1.1      0      16
Processing:     2   12   4.9     11      38
Waiting:        0   11   4.5     11      35
Total:          2   12   4.9     11      38

Percentage of the requests served within a certain time (ms)
  50%     11
  66%     13
  75%     15
  80%     16
  90%     19
  95%     22
  98%     26
  99%     29
 100%     38 (longest request)
