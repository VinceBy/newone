package com.example.myapplication;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class SecondActivity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        Log.d("SecondActivity", this.toString());
        Log.d("SecondActivity", "Task id is "+getTaskId());
        setContentView(R.layout.second_layout);

//        Intent intent = getIntent();
//        String data = intent.getStringExtra("extra_data");
//        Log.d("SecondActivity", data);//接受Ａｃｔｉｖｉｔｙ１中的数据并打印在Ｌｏｇ

        Button button2 = (Button) findViewById(R.id.button_2);
        button2.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                Toast.makeText(SecondActivity.this, "You click Button 2",
                        Toast.LENGTH_LONG).show();//点击后显示虚拟框
//                Intent intent  = new Intent();
//                intent.putExtra("data_return", "Hello FirstActivity");
//                setResult(RESULT_OK, intent);
//                finish();

                Intent intent = new Intent(SecondActivity.this, ThirdActivity.class);
                startActivity(intent);
            }
        });

    }
    public static void actionStart(Context context, String data1, String data2){
        Intent intent = new Intent(context,SecondActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        intent.putExtra("param1","data1");
        intent.putExtra("param2","data2");
        context.startActivity(intent);

//        Intent intent = new Intent(context, SecondActivity.class);
//        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//        intent.putExtra("param1","data1");
//        intent.putExtra("param2","data2");
//        context.startActivities(intent);
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d("SecondActivity", "onDestory");
    }
}
