package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;


public class VendingMachineImpl implements VendingMachine {
    private static int coins = 0;

    private static final Map<String,String> products = new HashMap<>();


    private static VendingMachine single_instance = null;


    public static VendingMachine getInstance() {

        if (single_instance == null) {
            single_instance = new VendingMachineImpl();
            createProducts();
        }

        return single_instance;
    }

    public static void createProducts(){
        products.put("ScottCola","75;true");
        products.put("KarenTea","100;false");
    }

    @Override
    public void insertQuarter() {
       coins += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

        if (!products.containsKey(name)) {
            throw new UnknownDrinkException();
        }

        String[] data = products.get(name).split(";");
        int price = Integer.parseInt(data[0]);
        boolean isfizzy = Boolean.parseBoolean(data[1]);

        if (coins >= price) {
            Drink drink = new DrinkImpl(name, isfizzy);
            coins -= price;
            return drink;
        } else {
            throw new NotEnoughMoneyException();
        }
    }

}
