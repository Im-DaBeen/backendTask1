package com.example.b201514099.model;

import lombok.Data;

@Data
public class Book {
    private String title;
    private String author;
    private Long categoryId;
    private Integer price;
} 