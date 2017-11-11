package main

import "github.com/gin-gonic/gin"
import "github.com/go-redis/redis"
import "encoding/json"

type CommonWord struct {
	Word  string
	Count int
}

type FmtStory struct {
	Title string `json:"title"`
	Description string `json:"description"`
	Story string `json:"story"`
	Image string `json:"image"`
}

type Story struct {
	URL         string       `json:"url"`
	Title       string       `json:"title"`
	Description string       `json:"desc"`
	Story       string       `json:"story"`
	CommonNouns []CommonWord `json:"commonNouns"`
	CommonAdjs  []CommonWord `json:"commonAdj"`
	Names       []string     `json:"names"`
}


func main() {
	r := gin.Default()
	r.Static("/static", "./dist/static")
	r.LoadHTMLFiles("dist/index.html")

	r.GET("/", func(c *gin.Context) {
		c.HTML(200, "index.html", nil)
	})
	r.GET("/images", func(c *gin.Context) {
		client := redis.NewClient(&redis.Options{
			Addr:     "redis:6379",
			Password: "",
			DB:       0,
		})

		img, err := client.Keys("*").Result()
		c.JSON(200, gin.H{
			"message": img,
			"other":   err,
		})
	})
	r.GET("/stories", func(c *gin.Context) {
		client := redis.NewClient(&redis.Options{
			Addr:     "redis:6379",
			Password: "", // no password set
			DB:       0,  // use default DB
		})

		key, err := client.RandomKey().Result()

		if err != nil {
			c.JSON(200, gin.H{
				"message": err,
			})

			return
		}

		value, _ := client.Get(key).Result()

		res := Story{}
		json.Unmarshal([]byte(value), &res)

		res2 := FmtStory{}

		res2.Title = res.Title
		res2.Description = res.Description
		res2.Story = res.Story
		res2.Image = "https://media.giphy.com/media/l41m0CPz6UCnaUmxG/giphy.gif"

		c.JSON(200, gin.H{
			"data": []FmtStory{res2},

		})
	})
	r.Run()
}
