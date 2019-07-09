package com.example.myapplication;

import android.content.Intent;
import android.icu.text.UnicodeSet;
import android.net.Uri;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class FirstActivity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        Log.d("FirstActivity",this.toString());
        Log.d("FirstActivity","Task id is "+getTaskId());
        setContentView(R.layout.first_layout);
        Button button1 = (Button) findViewById(R.id.button_1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(FirstActivity.this, "You click Button 1",
                        Toast.LENGTH_LONG).show();//点击后显示虚拟框

//                //finish();销毁当前活动

//                Intent intent = new Intent(FirstActivity.this, SecondActivity.class);
//                startActivity(intent);//显示Ｉｎｔｅｎｔ跳转到第二个activity

//                Intent intent = new Intent("com.example.myapplication.ACTION_START");
//                startActivity(intent);//隐式启动

//                Intent intent = new Intent("com.example.myapplication.ACTION_START");
//                intent.addCategory("com.example.myapplication.MY_CATEGORY");
//                startActivity(intent);

//                Intent intent = new Intent(Intent.ACTION_VIEW);
//                intent.setData(Uri.parse("http://www.baidu.com"));
//                startActivity(intent);//跳转百度页面

//                Intent intent = new Intent(Intent.ACTION_DIAL);
//                intent.setData(Uri.parse("tel:10086"));
//                startActivity(intent);//拨号

//                 String data = "Hello SecondActivity";
//                 Intent intent = new Intent(FirstActivity.this, SecondActivity.class);
//                 intent.putExtra("extra_data", data);
//                 startActivity(intent);//将Ａｃｔｉｖｉｔｙ１当中的数传给Ａｃｔｉｖｉｔｙ２

//                Intent intent = new Intent(FirstActivity.this, SecondActivity.class);
//                startActivityForResult(intent, 1);


//                    Intent intent = new Intent(FirstActivity.this, FirstActivity.class);
//                    startActivity(intent);

//                Intent intent = new Intent(FirstActivity.this, SecondActivity.class);
//                startActivity(intent);

                SecondActivity.actionStart(FirstActivity.this,"data1","data2");
            }
        });
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        switch(requestCode){
            case 1:
                if (resultCode == RESULT_OK){
                    String returnData = data.getStringExtra("data_return");
                    Log.d("FirstActivity", returnData);
                }
                break;
            default:
        }
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d("FirstActivity","onRestart");
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.add_item:
                Toast.makeText(this, "You clicked Add", Toast.LENGTH_SHORT).show();
                break;
            case R.id.remove_item:
                Toast.makeText(this, "You clicked Remove", Toast.LENGTH_SHORT).show();
                break;
            default:
            }
            return true;


    }
}
