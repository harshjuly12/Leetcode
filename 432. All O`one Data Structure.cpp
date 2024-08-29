class AllOne {
 public:
  void inc(string key) {
    const auto it = keyToIterator.find(key);

    if (it == keyToIterator.cend()) {
      if (l.empty() || l.front().value > 1)
        l.push_front({1, {key}});
      else
        l.front().keys.insert(key);
      keyToIterator[key] = l.begin();
      return;
    }

    const auto lit = it->second;   
    auto nit = next(lit);         

    if (nit == l.end() || nit->value > lit->value + 1)
      nit = l.insert(nit, {lit->value + 1, {key}});
    else  
      nit->keys.insert(key);
    keyToIterator[key] = nit;  

    lit->keys.erase(key);
    if (lit->keys.empty())
      l.erase(lit);
  }

  void dec(string key) {
    const auto it = keyToIterator.find(key);

    if (it == keyToIterator.cend())
      return;

    const auto lit = it->second;  

    if (lit->value == 1) {
      keyToIterator.erase(key);
    } else {
      auto pit = prev(lit); 

      if (lit == l.begin() || pit->value < lit->value - 1)
        pit = l.insert(lit, {lit->value - 1, {key}});
      else  
        pit->keys.insert(key);
      keyToIterator[key] = pit;  
    }

    lit->keys.erase(key);
    if (lit->keys.empty())
      l.erase(lit);
  }

  string getMaxKey() {
    return l.empty() ? "" : *l.back().keys.cbegin();
  }

  string getMinKey() {
    return l.empty() ? "" : *l.front().keys.cbegin();
  }

 private:
  struct Node {
    int value;
    unordered_set<string> keys;
  };

  list<Node> l;
  unordered_map<string, list<Node>::iterator> keyToIterator;
};