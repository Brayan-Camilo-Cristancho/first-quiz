package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink{

    private final String name;
    private final Boolean isFizzy;

    public DrinkImpl(String name, Boolean isFizzy) {
        this.name = name;
        this.isFizzy = isFizzy;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public boolean isFizzy() {
        return this.isFizzy;
    }
}
