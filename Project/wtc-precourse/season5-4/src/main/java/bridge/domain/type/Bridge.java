package bridge.domain.type;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Bridge {
    private static final String REPLACE_WORD = "O";
    private List<Direction> tiles = new ArrayList<Direction>();

    public Bridge() {
    }
    public Bridge(List<String> tiles) {
        // String U,D로 이루어진 List를 Direction List로 변환하여 등록
        this.tiles = tiles.stream()
                .map(Direction::from)
                .collect(Collectors.toList());
    }

    public List<String> getOneDirection(Direction direction) {
        return tiles.stream()
                .map(tile -> matchWithDirection(tile, direction))
                .collect(Collectors.toList());
    }

    private String matchWithDirection(Direction direction1, Direction direction2) {
        if (Direction.compare(direction1, direction2)) {
            return REPLACE_WORD;
        }
        return " ";
    }

    public void clear() {
        tiles.clear();
    }

    public void add(Direction direction) {
        tiles.add(direction);
    }

    public void add(String tile) {
        tiles.add(Direction.from(tile));
    }

    public boolean isRightWay(Bridge another) {
        List<Direction> anotherTiles = another.getTiles();

        for (int i = 0; i < tiles.size(); i++) {
            if (!isGoodDirection(tiles.get(i), anotherTiles.get(i))) {
                return false;
            }
        }
        return true;
    }

    private boolean isGoodDirection(Direction direction, Direction direction2) {
        if(direction == direction2) {
            return true;
        }
        return false;
    }

    private List<Direction> getTiles() {
        return tiles;
    }

    public boolean equals(Bridge bridge) {
        if (!isRightWay(bridge)) {
            return false;
        }
        if (tiles.size() != bridge.getTiles().size()) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return tiles.toString();
    }
}
