package com.example.listview;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;

public class FruitAdapter extends ArrayAdapter<Fruit> {

    private int resoureceId;

    public FruitAdapter(Context context, int textViewResourceId, List<Fruit> objects) {
        super(context, textViewResourceId, objects);
        resoureceId = textViewResourceId;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Fruit fruit = getItem(position);//获取当前项的Ｆｒｕｉｔ实例
        View view;
        ViewHolder viewHolder;
//        View view = LayoutInflater.from(getContext()).inflate(resoureceId, parent, false);
        if (convertView == null) {//判断是否第一次加载
            view = LayoutInflater.from(getContext()).inflate(resoureceId, parent, false);
            //缓存第一次加载的视图控件
            viewHolder = new ViewHolder();
            viewHolder.fruitImage = (ImageView) view.findViewById(R.id.fruit_image);
            viewHolder.fruitName = (TextView) view.findViewById(R.id.fruit_name);
            view.setTag(viewHolder);//将viewHolder存储在view中

        } else {
            view = convertView;
            viewHolder = (ViewHolder) view.getTag();//重新获取ＶｉｅｗＨｏｌｄｅｒ


        }
        viewHolder.fruitImage.setImageResource(fruit.getImageId());
        viewHolder.fruitName.setText(fruit.getName());
//        ImageView fruitImage = (ImageView) view.findViewById(R.id.fruit_image);
//        TextView fruitName = (TextView) view.findViewById(R.id.fruit_name);
//        fruitImage.setImageResource(fruit.getImageId());
//        fruitName.setText(fruit.getName());
        return view;

    }

}
