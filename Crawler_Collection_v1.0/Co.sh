docker run -v /home/Code/WULEWEI/Crawler_Collection/KTspider:/usr/src/wlw_test  -w /usr/src/wlw_test python_spider:spider_v1.2 python run.py && \cp /home/Code/WULEWEI/Crawler_Collection/KTspider/cp_data/data/* /home/admin/spider2flume/data/ && \cp /home/Code/WULEWEI/Crawler_Collection/KTspider/cp_data/logs/* /home/admin/spider2flume/log/ && mv /home/Code/WULEWEI/Crawler_Collection/KTspider/cp_data/data/* /home/Code/WULEWEI/Crawler_Collection/KTspider/data/ && mv /home/Code/WULEWEI/Crawler_Collection/KTspider/cp_data/logs/* /home/Code/WULEWEI/Crawler_Collection/KTspider/log/logs/


