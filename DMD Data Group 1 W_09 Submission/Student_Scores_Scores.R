#install.packages('tidyr')

library(dplyr) # For data manipulation
library(ggplot2) # For data visualization
library(tidyr) # For reshaping data


# ---------- Retrieving the Data

student_data <- read.csv("C:/Users/Capaciti/Downloads/student_scores.csv")


# 1. Missing values columns.
colSums(is.na(student_data))

# Dealing with missing values
student_data$math_score[is.na(student_data$math_score)] <- mean(student_data$math_score, na.rm = TRUE)
student_data$reading_score[is.na(student_data$reading_score)] <- mean(student_data$reading_score, na.rm = TRUE)
student_data$writing_score[is.na(student_data$writing_score)] <- mean(student_data$writing_score, na.rm = TRUE)

# Dealing with duplicated values
sum(duplicated(student_data$student_id))


# 2. Basic Descriptive Statistics


# 2.1 Feature Engineering: Aggregated Average Scores

#Feature Engineering

# Create new columns using mutate()
student_data <- mutate(student_data, student_tot_score = math_score + reading_score + writing_score)
student_data <- mutate(student_data, student_avg_score = (math_score + reading_score + writing_score) / 3)


#Students Who Passed got  more then  >= 50 in (Math, Reading, and Writing)
above_average_data <- student_data %>%
  filter(math_score >= 50, reading_score >= 50, writing_score >= 50)
print(above_average_data)

# Filtering the data by Females
female_data <- student_data %>%
  filter(gender == "Female")
print(female_data)

#Filtering the data by Males
male_data <- student_data %>%
  filter(gender == "Male")
print(male_data)


overall_averages <- student_data %>%
  summarise(
    avg_math = mean(math_score),
    avg_reading = mean(reading_score),
    avg_writing = mean(writing_score)
  )
print("Overall Average Scores:")
print(overall_averages)

# 2.2 Average Scores by Gender
gender_averages <- student_data %>%
  group_by(gender) %>%
  summarise(
    avg_math = mean(math_score),
    avg_reading = mean(reading_score),
    avg_writing = mean(writing_score)
  )
print("Average Scores by Gender:")
print(gender_averages)

# 2.3 Average Scores by School
school_averages <- student_data %>%
  group_by(school) %>%
  summarise(
    avg_math = mean(math_score),
    avg_reading = mean(reading_score),
    avg_writing = mean(writing_score)
  )
print("Average Scores by School:")
print(school_averages)

# 3. Visualization: Score Distribution Analysis

# 3.1 Histogram of Scores
ggplot(student_data, aes(x = math_score)) +
  geom_histogram(binwidth = 5, fill = "grey", color = "black") +
  ggtitle("Distribution of Math Scores") +
  xlab("Math Score") +
  ylab("Frequency")

ggplot(student_data, aes(x = reading_score)) +
  geom_histogram(binwidth = 5, fill = "grey", color = "black") +
  ggtitle("Distribution of Math Scores") +
  xlab("Reading Score") +
  ylab("Frequency")

ggplot(student_data, aes(x = writing_score)) +
  geom_histogram(binwidth = 5, fill = "grey", color = "black") +
  ggtitle("Distribution of Math Scores") +
  xlab("Writing Score") +
  ylab("Frequency")

# 3.2 Boxplot of Reading Scores by Gender
ggplot(student_data, aes(x = gender, y = reading_score)) +
  geom_boxplot(fill = "lightgreen") +
  ggtitle("Reading Scores by Gender") +
  xlab("Gender") +
  ylab("Reading Score")

# 3.3 Scatter Plot of Math Score vs. Reading Score
ggplot(student_data, aes(x = reading_score, y = math_score)) +
  geom_point(color = "purple") +
  geom_smooth(method = "lm", se = FALSE, color = "red") + # Add a regression line
  ggtitle("Math Score vs. Reading Score") +
  xlab("Reading Score") +
  ylab("Math Score")


# Bar plot showing the number of learners in each school
ggplot(student_data, aes(x = school)) +
  geom_bar(fill = "grey", color = "black") +
  ggtitle("Number of Learners in each School") +
  xlab("School") +
  ylab("Frequency")

# Bar plot of Females and Males
ggplot(student_data, aes(x = gender)) +
  geom_bar(fill = "grey", color = "black") +
  ggtitle("Number of Learners in each School") +
  xlab("Gender") +
  ylab("Frequency")



# 4. Advanced Analysis

# 4.1 Correlation Matrix
cor_matrix <- cor(student_data[, c("math_score", "reading_score", "writing_score")])
print("Correlation Matrix:")
print(cor_matrix)

# 4.2 Performance Summary by School and Gender
performance_summary <- student_data %>%
  group_by(school, gender) %>%
  summarise(
    avg_math = mean(math_score),
    avg_reading = mean(reading_score),
    avg_writing = mean(writing_score),
    n_students = n()
  )
print("Performance Summary by School and Gender:")
print(performance_summary)

# 4.3 Reshape data for plotting
long_data <- student_data %>%
  pivot_longer(
    cols = c(math_score, reading_score, writing_score),
    names_to = "subject",
    values_to = "score"
  )

# 4.4 Plotting the reshaped data.
ggplot(long_data, aes(x = subject, y = score, fill = gender)) +
  geom_boxplot() +
  facet_wrap(~school) +
  ggtitle("Score Distribution by Subject, Gender, and School") +
  xlab("Subject") +
  ylab("Score") #+
  #fill_discrete(name = "Gender")


