# Angular Test project paired with python-backend-test

## Based on [https://www.telerik.com/blogs/how-to-use-angular-create-next-level-ui-python-apps-why-do-it](https://www.telerik.com/blogs/how-to-use-angular-create-next-level-ui-python-apps-why-do-it)

## Corrections to the article

Where it talks about the code below

```typescript
import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
  providedIn: 'root'
})

constructor(private _http: HttpClient) { }

getdata() {
  return this._http.get('http://127.0.0.1:5000/api/data');
}
```

Use the code in app/app.component.ts instead. Which is the following

```typescript
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiserviceService } from './service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  newdata:any;

  constructor(private _apiservice:ApiserviceService) { }

  ngOnInit() {
	this.getData();
  }

  getData() {
	this._apiservice.getdata().subscribe(res=>{
  	this.newdata=res;
    if(this.newdata == undefined)
    {
      console.log("Failed to get python data");
    }
	})
  }
}
```

You also need to make changes to app/app.module.ts. You need to two lines.

This line near the top
```typescript
import {HttpClientModule} from '@angular/common/http';
```

Also add **HttpClientModule** to your imports array.

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import {HttpClientModule} from '@angular/common/http'; // add this line
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule // add this line
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

```

## Access-Control-Allow-Origin Error - two docker containers

Next Issue since I am using two docker containers one for angular and one for python.
I get an Access-Control-Allow-Origin Error.

I followed [https://www.stackhawk.com/blog/angular-cors-guide-examples-and-how-to-enable-it/](https://www.stackhawk.com/blog/angular-cors-guide-examples-and-how-to-enable-it/) to resolve the issue.

```
Access to XMLHttpRequest at 'http://127.0.0.1:5000/api/data' from origin 'http://127.0.0.1:4202' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

My first fix is adding the following to **serve** section of angular.json

```json
"options": {
	"browserTarget": "your-application-name:build",
	"proxyConfig": "src/proxy.conf.json"
	},
```

You also need to create **src/proxy.conf.json** and add the following to it.

```json
{
	"/api/data": {
	"target": "http://127.0.0.1:5000",
	"secure": false
	}
}
```

This didn't resolve the issue as it is an issue on the python end.


## Access-Control-Allow-Origin Error - python end

Instead of using the code provided by the article use the following

```python
from flask import Flask, jsonify

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/data', methods=['GET'])
def get_data():
	data = {
		'title': 'Welcome to Angular-Python App',
		'message': 'This is an example integration between Angular and Python!'
	}
	response = jsonify(data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0')
```