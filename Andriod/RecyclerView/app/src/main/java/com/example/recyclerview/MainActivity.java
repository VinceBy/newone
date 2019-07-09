package com.example.recyclerview;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.StaggeredGridLayoutManager;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MainActivity extends AppCompatActivity {
    private List<Fruit> fruitList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initFruits();//初始化水果参数
        RecyclerView recyclerView =(RecyclerView)findViewById(R.id.recycler_view);
        StaggeredGridLayoutManager layoutManager = new
                StaggeredGridLayoutManager(3, StaggeredGridLayoutManager.VERTICAL);
//        LinearLayoutManager layoutManager = new LinearLayoutManager(this);
//        layoutManager.setOrientation(LinearLayoutManager.HORIZONTAL);
        recyclerView.setLayoutManager(layoutManager);
        FruitAdapter adapter = new FruitAdapter(fruitList);
        recyclerView.setAdapter(adapter);
    }

    private void initFruits() {
        for (int i=0; i<2; i++){
            Fruit apple = new Fruit(getRandomLengthName("Apple"), R.drawable.ad3d397152ce30a0517fa808335dea19c7b453f6);
            fruitList.add(apple);
            Fruit banana = new Fruit(getRandomLengthName("banana"), R.drawable.b172eef69885e865bf5c108ff5310fc4223e5ac4);
            fruitList.add(banana);
            Fruit orange = new Fruit(getRandomLengthName("orange"), R.drawable.d5c229c28c1668d12f5abaeccea5d983036984a4);
            fruitList.add(orange);
            Fruit watermelon = new Fruit(getRandomLengthName("watermelon"), R.drawable.ad3d397152ce30a0517fa808335dea19c7b453f6);
            fruitList.add(watermelon);
            Fruit pear = new Fruit(getRandomLengthName("pear"), R.drawable.d5c229c28c1668d12f5abaeccea5d983036984a4);
            fruitList.add(pear);
            Fruit grape = new Fruit(getRandomLengthName("grape"), R.drawable.b172eef69885e865bf5c108ff5310fc4223e5ac4);
            fruitList.add(grape);
            Fruit pineapple = new Fruit(getRandomLengthName("pineapple"), R.drawable.ecf107f93e1ce947a3eb4dc7dada4a6cb8c15778);
            fruitList.add(pineapple);
            Fruit cherry = new Fruit(getRandomLengthName("cherry"), R.drawable.d5c229c28c1668d12f5abaeccea5d983036984a4);
            fruitList.add(cherry);
            Fruit mango = new Fruit(getRandomLengthName("mango"), R.drawable.b172eef69885e865bf5c108ff5310fc4223e5ac4);
            fruitList.add(mango);
        }
    }

    private String getRandomLengthName(String name) {
        Random random = new Random();
        int length = random.nextInt(20)+1;
        StringBuilder builder = new StringBuilder();
        for(int i = 0;i < length; i++){
            builder.append(name);
        }
        return builder.toString();
    }
}
