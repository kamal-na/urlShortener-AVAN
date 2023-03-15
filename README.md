<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Url Shortener API
</h1>

> Url shortener API with Django and django rest framework and MongoDB.


How Url Shortener API Works:
- You can send (POST) a full url and retrieve a small encoded one with tier.app as the base web service url.

    Eg. POST http://localhost:8000/shorten-url
    with 
        
    ```
    https://www.farsnews.ir/news/14011216000365/%D9%82%D8%B1%D8%B9%D9%87-%DA%A9%D8%B4%DB%8C-%D8%AC%D8%A7%D9%85-%D8%AD%D8%B0%D9%81%DB%8C-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%D8%B4%D8%AF%7C-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AF%D8%B1-%D8%AC%D9%85-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3-%D8%AF%D8%B1-%D8%A7%D9%86%D8%AA%D8%B8%D8%A7%D8%B1-%D8%A8%D8%B1%D9%86%D8%AF%D9%87
    ```

    result: 
        
    ```
    https://yun.ir/7svkz3 (6 digits id)
    ```
    
- You can get the original url with the encoded url on a GET request (done in previous step)

    Eg. GET https://yun.ir/7svkz3
    result: 
        
    ```
    https://www.farsnews.ir/news/14011216000365/%D9%82%D8%B1%D8%B9%D9%87-%DA%A9%D8%B4%DB%8C-%D8%AC%D8%A7%D9%85-%D8%AD%D8%B0%D9%81%DB%8C-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%D8%B4%D8%AF%7C-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AF%D8%B1-%D8%AC%D9%85-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3-%D8%AF%D8%B1-%D8%A7%D9%86%D8%AA%D8%B8%D8%A7%D8%B1-%D8%A8%D8%B1%D9%86%D8%AF%D9%87
    ```
        

<br><br>


## USAGE
#### 1. Endpoint List
URI Example: `http://localhost:8000/shorten-url/`

```
body: {'url':'https://www.farsnews.ir/news/14011216000365/%D9%82%D8%B1%D8%B9%D9%87-%DA%A9%D8%B4%DB%8C-%D8%AC%D8%A7%D9%85-%D8%AD%D8%B0%D9%81%DB%8C-%D8%A7%D9%86%D8%AC%D8%A7%D9%85-%D8%B4%D8%AF%7C-%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AF%D8%B1-%D8%AC%D9%85-%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3-%D8%AF%D8%B1-%D8%A7%D9%86%D8%AA%D8%B8%D8%A7%D8%B1-%D8%A8%D8%B1%D9%86%D8%AF%D9%87'}
```

| | Available Methods | URI | Example URL |
| -: | :- | :- | -: |
| | | | |
| | **Project Endpoints** | | |
| 1. | `POST` | `shorten-url/` | `http://localhost:8000/shorten-url` |
| 2. | `GET`  | `/<short_id>` | `http://localhost:8000/<short_id>` |


<br>

  #### Notice: You must be authorize to post and generate short url.
  for this job I recommended to use postman and use below usernam and password.

  ```
  username: admin
  pass: admin
  ```

<br>

<br>

  #### Test
  I add multiple test for testing and for this job you can run below command:

  ```
  python manage.py test
  ```

<br>