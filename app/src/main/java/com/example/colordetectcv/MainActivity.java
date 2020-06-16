package com.example.colordetectcv;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.Color;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import static com.example.colordetectcv.R.id.image;

public class MainActivity extends AppCompatActivity {


    ImageView mImageView;
    TextView mResultTv;
    View mColorView;

    Bitmap bitmap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mImageView = findViewById(R.id.imageView);
        mResultTv = findViewById(R.id.resultTv);
        mColorView = findViewById(R.id.colorView);

        mImageView.setDrawingCacheEnabled(true);
        mImageView.buildDrawingCache(true);

        //Image view on touch listener
        mImageView.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                if (event.getAction() == MotionEvent.ACTION_DOWN || event.getAction() == MotionEvent.ACTION_MOVE){
                    bitmap = mImageView.getDrawingCache();

                    int pixel = bitmap.getPixel((int)event.getX(), (int)event.getY());

                    //getting RGB value
                    int r = Color.red(pixel);
                    int g = Color.green(pixel);
                    int b = Color.blue(pixel);

                    //getting Hex value
                    String hex = "#" + Integer.toHexString(pixel);

                    //change RGB to XYZ
                    double X = 0.43057*r + 0.34155*g + 0.17832*b;
                    double Y = 0.22201*r + 0.70665*g + 0.07133*b;
                    double Z = 0.02018*r + 0.12995*g + 0.93918*b;

                    //change XYZ to xyz
                    double x = X/(X+Y+Z);
                    double y = Y/(X+Y+Z);
                    double z = 1-x-y;

                    //set background color of view according to the picked color
                    mColorView.setBackgroundColor(Color.rgb(r, g, b));
                    //set RGB, HEX values to textview
                    mResultTv.setText("HEX: " + hex
                            + "\nRGB: " + r + ", " + g + ", " + b
                            + "\nXYZ: " + X + ", " + Y + ", " + Z
                            + "\nxyz: " + x + ", " + y + ", " + z );

                }
                return true;
            }
        });
    }
}