package com.example.listview;

import android.support.annotation.NonNull;
import android.support.v4.app.TaskStackBuilder;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
//    private String[] data = {
//            "Apple", "Banana", "Orange", "Watermelon", "Pear", "Grape", "Pineapple",
//            "Strawberry", "Cherry", "Mango", "Apple", "Banana",  "Orange", "Watermelon",
//            "Pear", "Grape", "Pineapple", "Strawberry", "Cherry", "Mango"
//    };

    private List<Fruit> fruitList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initFruits();//初始化水果参数
        FruitAdapter adapter = new FruitAdapter(MainActivity.this, R.layout.fruit_item, fruitList);
        ListView listView = (ListView) findViewById(R.id.list_view);
        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Fruit fruit = fruitList.get(position);
                Toast.makeText(MainActivity.this, fruit.getName(), Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void initFruits() {
        for (int i=0; i<2; i++){
            Fruit apple = new Fruit("Apple", R.drawable.ad3d397152ce30a0517fa808335dea19c7b453f6);
            fruitList.add(apple);
            Fruit banana = new Fruit("banana", R.drawable.b172eef69885e865bf5c108ff5310fc4223e5ac4);
            fruitList.add(banana);
            Fruit orange = new Fruit("orange", R.drawable.d5c229c28c1668d12f5abaeccea5d983036984a4);
            fruitList.add(orange);
            Fruit watermelon = new Fruit("watermelon", R.drawable.ad3d397152ce30a0517fa808335dea19c7b453f6);
            fruitList.add(watermelon);
            Fruit pear = new Fruit("pear", R.drawable.d5c229c28c1668d12f5abaeccea5d983036984a4);
            fruitList.add(pear);
            Fruit grape = new Fruit("grape", R.drawable.b172eef69885e865bf5c108ff5310fc4223e5ac4);
            fruitList.add(grape);
            Fruit pineapple = new Fruit("pineapple", R.drawable.ecf107f93e1ce947a3eb4dc7dada4a6cb8c15778);
            fruitList.add(pineapple);
            Fruit cherry = new Fruit("cherry", R.drawable.d5c229c28c1668d12f5abaeccea5d983036984a4);
            fruitList.add(cherry);
            Fruit mango = new Fruit("mango", R.drawable.b172eef69885e865bf5c108ff5310fc4223e5ac4);
            fruitList.add(mango);
        }
    }


}
