#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <string>
#include <chrono>
#include <curl/curl.h>


size_t write_data(void *buffer, size_t size, size_t nmemb, void *userp)
{
	return size * nmemb;
}

int main(int argc, char *argv[]) {

	if (argc != 4) {
		std::cout << "Usage: http-curl <server> <path> <port>\n";
		return 1;
	}

	long bytes = 0;

	auto start =
		std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();

	CURL *curl;
	CURLcode res;

	curl_global_init(CURL_GLOBAL_DEFAULT);

	curl = curl_easy_init();
	if (curl) {

		std::string url = "";
		std::string server = std::string(argv[1]);
		std::string path = std::string(argv[2]);
		std::string port = std::string(argv[3]);
		url = "https://" + server + ":" + port + "/" + path;

		curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
		curl_easy_setopt(curl, CURLOPT_PORT, port);
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);
		curl_easy_setopt(curl, CURLOPT_SSL_SESSIONID_CACHE, 0L);

		std::cout << url << std::endl;

		/* Perform the request, res will get the return code */
		res = curl_easy_perform(curl);

		/* Check for errors */
		if (res != CURLE_OK) {
			std::cout << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
		} else {
			int res2 = curl_easy_getinfo(curl, CURLINFO_SIZE_DOWNLOAD_T, &bytes);
		}

		/* always cleanup */
		curl_easy_cleanup(curl);
	}

	curl_global_cleanup();

	auto stop =
		std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();

	auto elapsed = stop - start;
	auto rate = bytes * 8.0f * 1000.0f / (elapsed * 1024.0f * 1024.0f);
	std::cout << "time: " << elapsed << ", bytes: " << bytes << ", rate: " << rate << std::endl;

	std::ofstream output;
	output.open("out");
	output << "Content-Length: " << bytes << "\n";
	output << "Rate: " << rate << "\n";
	output << "Start: " << start << "\n";
	output << "Stop: " << stop << "\n";
	output.close();

	return 0;
}