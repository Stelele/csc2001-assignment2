/**
 * class that stores the data for a given entry
 * */
public class LSData implements Comparable<LSData>
{
    private String area;
    private String regions;
    
    /**
     * @param area <code>String</code> represents the key fieild of object
     * @param regions <code>String</code> represents the various regions for the specified key
     * */
    public LSData(String area, String regions)
    {
        this.area = area;
        this.regions = regions;
    }
    
    /**
     * @return area <code>String</code> represents the key field of the object
     * */
    public String getArea()
    {
        return area;
    }
    
    /**
     * @return regions <code>String</code> represents the various regions of the specified key
     * */
    public String getRegions()
    {
        return regions;
    }
    
    /**
     * @param area <code>String</code> represents new key field for given object
     * */
    public void setArea(String area)
    {
        this.area = area;
    }
    
    /**
     * @param regions <code>String</code> represents new regions for specified key
     * */
    public void setRegions(String regions)
    {
        this.regions = regions;
    }
    
    /**
     * @return value <code>String</code> represents string representation of the object properties
     * */
    public String toString()
    {
        return area.toString() + " " + regions.toString();
    }
    
    /**
     * function that compares the key field of the LSData class
     * @param data <code>LSData<String></code> represents the object to be compared to with
     * @return comparison <code>int<code> represent the result of the key comparisons
     * */
    public int compareTo(LSData data)
    {
        return area.compareTo(data.area);
    }
}
