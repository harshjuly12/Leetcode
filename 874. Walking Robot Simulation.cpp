class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0, y = 0;
        int direction = 0;
        int maxDistance = 0;
        
        set<pair<int, int>> obstacleSet;
        for (const auto& obs : obstacles) {
            obstacleSet.insert({obs[0], obs[1]});
        }
        
        for (int command : commands) {
            if (command == -2) {
                direction = (direction + 3) % 4;
            } else if (command == -1) {
                direction = (direction + 1) % 4;
            } else {
                for (int i = 0; i < command; ++i) {
                    int nx = x + directions[direction].first;
                    int ny = y + directions[direction].second;
                    
                    if (obstacleSet.find({nx, ny}) != obstacleSet.end()) {
                        break;
                    }
                    
                    x = nx;
                    y = ny;
                    
                    maxDistance = max(maxDistance, x * x + y * y);
                }
            }
        }
        
        return maxDistance;
    }
};