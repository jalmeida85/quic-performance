package com.test;

import java.io.*;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class HttpClient {

  public static void main(String[] args) throws IOException {

    if (args.length != 3) {
      System.out.println("Usage: http-curl <server> <path> <port>");
      System.exit(1);
    }

    OkHttpClient client = new OkHttpClient();
    long contentLength = 0;
    String server = args[0];
    String file = args[1];
    String port = args[2];
    String url = "https://" + server + ":" + port + "/speedtest/" + file;

    System.out.println("URL --> " + url);
    long start = System.currentTimeMillis();

    Request request = new Request.Builder().url(url).build();

    try {
      Response response = client.newCall(request).execute();
      contentLength = response.body().contentLength();
      response.body().bytes();
      response.body().close();
    } catch (Exception e) {
      e.printStackTrace();
    }

    long end = System.currentTimeMillis();
    long time = end - start;
    double rate = (contentLength * 8.0 / 1024.0 / 1024.0) / (time / 1000.0);

    System.out.println("Content-Length: " + contentLength + ", Rate: " + rate + ", Time: " + time);

    try {
      FileWriter fw = new FileWriter("out");
      fw.write("Content-Length: " + contentLength + "\n");
      fw.write("Rate: " + rate + "\n");
      fw.write("Time: " + time + "\n");
      fw.write("Start: " + start + "\n");
      fw.write("Stop: " + end);
      fw.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
